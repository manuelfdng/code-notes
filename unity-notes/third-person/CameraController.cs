using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public bool cursorLocked;

    private float pitch;
    private float yaw;
    public float mouseSensitivity = 1f;

    private Vector3 currentRotation;

    public Transform objectToFollow;

    private Vector3 rotationSmoothVelocity;
    public float rotationSmoothTime = 0.12f;
    public float distToObject = 3f;

    void Start()
    {
        if (cursorLocked)
        {
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;
        }
    }

    void LateUpdate()
    {
        yaw += Input.GetAxis("Mouse X") * mouseSensitivity;
        pitch -= Input.GetAxis("Mouse Y") * mouseSensitivity;

        currentRotation = Vector3.SmoothDamp(currentRotation, new Vector3(pitch, yaw), ref rotationSmoothVelocity, rotationSmoothTime);

        transform.eulerAngles = currentRotation;

        transform.position = objectToFollow.position - transform.forward * distToObject;

    }
}
