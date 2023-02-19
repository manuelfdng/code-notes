using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    public static Menu menu;
    public GameObject[] cardisp;
    public GameObject[] workingCars;

    public Transform cardisp_pos1;
    public Transform cardisp_pos2;

    public Camera menuCamera;
    public Camera carCamera;
    public Transform targetCamPos;
    public Transform mainCamPos;

    public int cardisp_ind1 = 0;
    public int cardisp_ind2 = 0;
    int map_ind = 0;

    GameObject t_disp1;
    GameObject t_disp2;


    public string[] maps;
    public TMP_Text mapName;

    private void Start()
    {
        DontDestroyOnLoad(gameObject);
    }
    public void PlayGame()
    {
        SceneManager.LoadScene(map_ind + 1);
    }

    // Update is called once per frame
    public void QuitGame()
    {
        Debug.Log("QUIT");
        Application.Quit();
    }

    public void MoveToCarSelection()
    {
        menuCamera.transform.position = targetCamPos.position;
        carCamera.transform.position = targetCamPos.position;

        menuCamera.transform.rotation = targetCamPos.rotation;
        carCamera.transform.rotation = targetCamPos.rotation;

        t_disp1 = Instantiate(cardisp[cardisp_ind1], cardisp_pos1.position, cardisp_pos1.rotation) as GameObject;
        t_disp2 = Instantiate(cardisp[cardisp_ind2], cardisp_pos2.position, cardisp_pos2.rotation) as GameObject;

        mapName.text = maps[map_ind];

    }

    public void MoveToMainPosition()
    {
        menuCamera.transform.position = mainCamPos.position;
        carCamera.transform.position = mainCamPos.position;

        menuCamera.transform.rotation = mainCamPos.rotation;
        carCamera.transform.rotation = mainCamPos.rotation;

        Destroy(t_disp1);
        Destroy(t_disp2);

        mapName.text = maps[map_ind];

    }

    public void ChangeDisplayForward1()
    {
        Destroy(t_disp1);
        cardisp_ind1++;
        if (cardisp_ind1 == 5) cardisp_ind1 -= 5;
        t_disp1 = Instantiate(cardisp[cardisp_ind1], cardisp_pos1.position, cardisp_pos1.rotation) as GameObject;
       

    }

    public void ChangeDisplayBackward1()
    {

        Destroy(t_disp1);
        cardisp_ind1--;
        if (cardisp_ind1 == -1) cardisp_ind1 += 5;
        t_disp1 = Instantiate(cardisp[cardisp_ind1], cardisp_pos1.position, cardisp_pos1.rotation) as GameObject;

    }

    public void ChangeDisplayForward2()
    {
        Destroy(t_disp2);
        cardisp_ind2++;
        if (cardisp_ind2 == 5) cardisp_ind2 -= 5;
        t_disp2 = Instantiate(cardisp[cardisp_ind2], cardisp_pos2.position, cardisp_pos2.rotation) as GameObject;


    }

    public void ChangeDisplayBackward2()
    {

        Destroy(t_disp2);
        cardisp_ind2--;
        if (cardisp_ind2 == -1) cardisp_ind2 += 5;
        t_disp2 = Instantiate(cardisp[cardisp_ind2], cardisp_pos2.position, cardisp_pos2.rotation) as GameObject;

    }

    public void ChangeSceneForward()
    {
        map_ind++;
        if (map_ind == 3) map_ind -= 3;
        mapName.text = maps[map_ind];
    }
    public void ChangeSceneBackward()
    {
        map_ind--;
        if (map_ind == -1) map_ind += 3;
        mapName.text = maps[map_ind];
    }

}
