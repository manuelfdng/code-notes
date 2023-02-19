using System.Collections;
using System.Collections.Generic;
using UnityEditor.Experimental.GraphView;
using UnityEngine;

public class FPScontroller : MonoBehaviour
{
    public bool cursorLocked;
    public Transform camera;

    public float camRotationSpeed = 5f;
    public float CameraMinimumY = -60f;
    public float cameraMaximumY = 75f;
    public float rotationSmoothSpeed = 10f;

    public float walkSpeed = 9f;
    public float runSpeed = 14f;
    public float maxSpeed = 20f;
    public float jumpPower = 30f;

    public float extraGravity = 45f;

    float bodyRotationX;
    float bodyRotationY;

    float camRotationY;
    Vector3 directionIntentX;
    Vector3 directionIntentY;
    float speed;

    public bool isGrounded;

    Rigidbody rb;

    void Start()
    {
        if (cursorLocked)
        {
            Cursor.lockState = CursorLockMode.Confined;
            Cursor.visible = false;
        } 
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        LookRotation();
        Movement();
    }

    void LookRotation()
    {
        bodyRotationX += Input.GetAxis("Mouse X") * camRotationSpeed;
        camRotationY += Input.GetAxis("Mouse Y") * camRotationSpeed;

        camRotationY = Mathf.Clamp(camRotationY, CameraMinimumY, cameraMaximumY);

        Quaternion camTargetRotation = Quaternion.Euler(-camRotationY, 0, 0);
        Quaternion bodyTargetRotation = Quaternion.Euler(0, bodyRotationX, 0);

        transform.rotation = Quaternion.Lerp(transform.rotation, bodyTargetRotation, Time.deltaTime * rotationSmoothSpeed);
        camera.localRotation = Quaternion.Lerp(camera.localRotation, camTargetRotation, Time.deltaTime * rotationSmoothSpeed);
    }

    void Movement()
    {
        directionIntentX = camera.right;
        directionIntentX.y = 0;
        directionIntentX.Normalize();

        directionIntentY = camera.forward;
        directionIntentY.y = 0;
        directionIntentX.Normalize();

        rb.velocity = directionIntentY * Input.GetAxis("Vertical") * speed + directionIntentX * Input.GetAxis("Horizontal") * speed + Vector3.up * rb.velocity.y;
        rb.velocity = Vector3.ClampMagnitude(rb.velocity, maxSpeed);

        if(Input.GetKey(KeyCode.LeftShift))
        {
            speed = runSpeed;
        }        
        if(!Input.GetKey(KeyCode.LeftShift))
        {
            speed = walkSpeed;
        }
    }
}
