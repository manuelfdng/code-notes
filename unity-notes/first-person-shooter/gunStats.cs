using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "New Gun", menuName = "Gun")]
public class gunStats : ScriptableObject
{
    public string gunName;
    public GameObject gunModel;

    public float kickback;
    public float recoil;
    public float swayFrequency;
    public float swayAmplitude;

    public float aimSpeed;
    public float aimSwayModifier;
    public float timeBetweenShots;
    public int bulletSpray;
}
