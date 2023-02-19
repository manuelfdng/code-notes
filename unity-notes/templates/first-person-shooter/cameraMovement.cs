using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cameraMovement : MonoBehaviour
{
    float mouseX;
    float mouseY;

    float rotationX;
    float rotationY;
    float cacheY;

    [SerializeField]
    float mouseSensitivity = 100f;

    public GameObject playerBody;

    void Start()
    {
        
    }

    void Update()
    {
        GetMouseInputs();
        rotationY = mouseY * mouseSensitivity * Time.deltaTime;
        rotationX = mouseX * mouseSensitivity * Time.deltaTime;
        cacheY -= rotationY;
        transform.localRotation = Quaternion.Euler(cacheY, 0, 0);
        playerBody.transform.Rotate(rotationX * Vector3.up);
    }

    void GetMouseInputs()
    {
        mouseX = Input.GetAxis("Mouse X");
        mouseY = Input.GetAxis("Mouse Y");
    }
}
