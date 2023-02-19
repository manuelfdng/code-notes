using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;
using System.Threading;
using UnityEngine.Experimental.UIElements;

public class SceneController : MonoBehaviour
{

    public Transform spawn1;
    public Transform spawn2;
    private TMP_Text countdown;

    public TMP_Text car1laps;
    public TMP_Text car2laps;
    public GameObject victoryMessage;
    public TMP_Text winnerName;

    public Camera camera1;
    public Camera camera2;

    GameObject manager;
    Menu menu;

    public GameObject car1;
    public GameObject car2;

    float counter = 6f;

    public bool canDrive = false;


    void Start()
    {
        manager = GameObject.Find("Manager");
        menu = manager.GetComponent<Menu>();
        countdown = GameObject.Find("Start").GetComponentInChildren<TMP_Text>();

        car1 = Instantiate(menu.workingCars[menu.cardisp_ind1], spawn1.position, spawn1.rotation) as GameObject;
        car2 = Instantiate(menu.workingCars[menu.cardisp_ind2], spawn2.position, spawn2.rotation) as GameObject;
        camera1.GetComponent<CarCamera>().objectToFollow = car1.transform;
        camera2.GetComponent<CarCamera>().objectToFollow = car2.transform;


        car1.GetComponent<CarController>().isPlayer1 = true;


    }

    private void Update()
    {
        if (counter > 1)
        {
            counter -= Time.deltaTime;
            countdown.text = "Ready in " + Mathf.Round(counter);
        }
        else if (counter < 1 && counter >= -2) 
        {
            canDrive = true;
            counter -= Time.deltaTime;
            countdown.text = "GO!";
        }

        else
        {
            countdown.text = null;
        }

        if (car1.GetComponent<CarController>().lapCounter >= 4) car1laps.text = "Laps: 3/3";
        else car1laps.text = "Laps: " + car1.GetComponent<CarController>().lapCounter + "/3";

        if (car2.GetComponent<CarController>().lapCounter >= 4) car2laps.text = "Laps: 3/3";
        else car2laps.text = "Laps: " + car2.GetComponent<CarController>().lapCounter + "/3";

        if (car1.GetComponent<CarController>().lapCounter >= 4 || car2.GetComponent<CarController>().lapCounter >= 4)
        {
            if (car1.GetComponent<CarController>().lapCounter > car2.GetComponent<CarController>().lapCounter)
            {
                winnerName.text = "P1 wins!";
            }

            else
            {
                winnerName.text = "P2 wins!";
            }

            victoryMessage.SetActive(true);

            if (Input.GetKeyDown(KeyCode.Escape)) SceneManager.LoadScene(0);
        }



    }



}
