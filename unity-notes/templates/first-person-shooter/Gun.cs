using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gun : MonoBehaviour
{
    #region variables
    public gunStats[] gunStatsList;
    GameObject equippedGun;

    public GameObject bulletHoleRef;
    [SerializeField]
    Transform weaponSpawnTransform;

    bool changeTo_1;
    bool changeTo_2;
    bool changeTo_3;

    bool isAiming;
    bool isShooting;

    int changeGunQuery;
    int currentGunIndex = 10;

    RaycastHit Hit;
    public LayerMask canBeShot;

    //Hold gunStats 
    float aimSpeed;
    float swayAmplitude;
    float swayFrequency;
    float aimSwayModifierTemp;
    float aimSwayModifier;

    Transform currentWeaponPosition;
    Transform hipFireTransform;
    Transform aimFireTransform;
    #endregion

    void Start()
    {
        weaponSpawnTransform = transform;
    }

    void Update()
    {
        GetGunInputs();

        //Change Weapon
        if (changeTo_1 || changeTo_2 || changeTo_3)
        {
            changeGunQuery = changeTo_1 ? 0 : changeTo_2 ? 1 : changeTo_3 ? 2 : 0;

            if(changeGunQuery != currentGunIndex) { ChangeGun(changeGunQuery); }

        }

        //Aim Weapon
        AimGun();

        //Shoot Weapon
        if (isShooting) { ShootGun(); }

        //Sway Weapon
        AnimateGun();

    }

    void GetGunInputs()
    {
        changeTo_1 = Input.GetKeyDown(KeyCode.Alpha1);
        changeTo_2 = Input.GetKeyDown(KeyCode.Alpha2);
        changeTo_3 = Input.GetKeyDown(KeyCode.Alpha3);

        isAiming = Input.GetKey(KeyCode.Mouse1);
        isShooting = Input.GetKeyDown(KeyCode.Mouse0);

    }

    void ChangeGun(int gunSelection)
    {
            currentGunIndex = gunSelection;

            Destroy(equippedGun); 

            equippedGun = Instantiate(gunStatsList[currentGunIndex].gunModel, weaponSpawnTransform);
            
            currentWeaponPosition = GameObject.Find("Player/Main Camera/Weapon/" + 
                                                    gunStatsList[currentGunIndex].gunName.ToString()  + 
                                                    "(Clone)/currentWeaponPosition").transform;

            hipFireTransform = GameObject.Find("Player/Main Camera/Weapon/" +
                                                gunStatsList[currentGunIndex].gunName.ToString() + 
                                                "(Clone)/States/Hip").transform;

            aimFireTransform = GameObject.Find("Player/Main Camera/Weapon/"
                                                + gunStatsList[currentGunIndex].gunName.ToString() + 
                                                "(Clone)/States/ADS").transform;

            ModifyGunStats(currentGunIndex);   

    }

    void ModifyGunStats(int gunStatsQuery)
    {
        aimSpeed = gunStatsList[gunStatsQuery].aimSpeed;
        swayAmplitude = gunStatsList[gunStatsQuery].swayAmplitude;
        swayFrequency = gunStatsList[gunStatsQuery].swayFrequency;
        aimSwayModifierTemp = gunStatsList[gunStatsQuery].aimSwayModifier;

    }

    void AimGun()
    {
        if (equippedGun != null)
        {
            if (isAiming)
            {
                currentWeaponPosition.position = Vector3.Lerp(currentWeaponPosition.position, aimFireTransform.position, aimSpeed);

            }
            else
            {
                currentWeaponPosition.position = Vector3.Lerp(currentWeaponPosition.position, hipFireTransform.position, aimSpeed);
            }
        }
    }

    void ShootGun()
    {
        if(Physics.Raycast(transform.position, transform.forward, out Hit, 100f, canBeShot))
        {
            GameObject bulletHole = Instantiate(bulletHoleRef, Hit.point + (Hit.normal * 0.01f), Quaternion.identity);
            bulletHole.transform.LookAt(Hit.point + Hit.normal);
            Destroy(bulletHole, 5f);

            if(Hit.collider.CompareTag("Crate"))
            {
                Hit.collider.gameObject.GetComponent<Crate>().Explode();
            }
        }

    }

    void AnimateGun()
    {
        aimSwayModifier = (isAiming)? aimSwayModifierTemp : 1;

        weaponSpawnTransform.localPosition = new Vector3(Mathf.Cos(Time.time * swayFrequency * 0.5f) * swayAmplitude * 2f * aimSwayModifier,
                                                        Mathf.Sin(Time.time * swayFrequency) * swayAmplitude * aimSwayModifier,
                                                        0);
        
    }

    
}
