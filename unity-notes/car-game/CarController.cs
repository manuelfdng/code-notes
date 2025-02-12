using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public enum Axel
{
    Front,
    Rear
}

[Serializable]
public struct Wheel
{
    public GameObject model;
    public WheelCollider collider;
    public Axel axel;
}

public class CarController : MonoBehaviour
{
    public List<Wheel> wheels;
    public float motorTorque;
    public float steerAngle;
    public bool isPlayer1;

    Rigidbody rb;
    public Vector3 COM;
    private float motor;
    private float steering;
    public float steerSmooth;
    private bool isBraking;
    public float brakeForce;

    GameObject sceneController;
    SceneController sceneScript;

    public int lapCounter = 0;

    void Start()
    {
        sceneController = GameObject.Find("SceneController");
        sceneScript = sceneController.GetComponent<SceneController>();
        rb = GetComponent<Rigidbody>();
        rb.centerOfMass = COM;
    }

    void FixedUpdate()
    {
        if (isPlayer1)
        {
            if (sceneScript.canDrive == false) return;
            
            motor = Input.GetAxis("Vertical") * motorTorque;
            steering = Input.GetAxis("Horizontal") * steerAngle;
            isBraking = Input.GetKey(KeyCode.Q);

        }
        else
        {
            if (sceneScript.canDrive == false) return;

            motor = Input.GetAxis("Vertical2") * motorTorque;
            steering = Input.GetAxis("Horizontal2") * steerAngle;
            isBraking = Input.GetKey(KeyCode.RightShift);
        }

        foreach (Wheel wheel in wheels)
        {
            wheel.collider.ConfigureVehicleSubsteps(30, 10, 3);

            wheel.collider.motorTorque = motor;

            if (wheel.axel == Axel.Front) wheel.collider.steerAngle = Mathf.Lerp(wheel.collider.steerAngle, steering, steerSmooth);

            if (isBraking) wheel.collider.brakeTorque = brakeForce;
            else wheel.collider.brakeTorque = 0f;

            wheel.collider.GetWorldPose(out Vector3 pos, out Quaternion rot);
            
            wheel.model.transform.position = pos;
            wheel.model.transform.rotation = rot * Quaternion.Euler(0, 90, 0);

        }

    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.name == "Start") lapCounter++;
    }
}
