using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float walkSpeed = 2f;
    public float runSpeed = 6f;

    private bool isJumping;
    private float y_vel;
    public float jumpHeight = 1f;
    public float gravity = -12f;

    public float turnSmoothTime = 0.2f;
    private float turnSmoothVelocity;

    public float speedSmoothTime = 0.1f;
    private float speedSmoothVelocity;
    private float currentSpeed;
    private float refSpeed;

    private Animator animator;
    private Transform cam;

    private CharacterController controller;

    void Start()
    {
        animator = GetComponent<Animator>();
        cam = Camera.main.transform;
        controller = GetComponent<CharacterController>();
    }

    void Update()
    {
        Vector2 input = new Vector2(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"));
        isJumping = Input.GetKeyDown(KeyCode.Space);

        Vector2 inputDir = input.normalized;

        if (inputDir != Vector2.zero)
        {
            float targetRotation = Mathf.Atan2(inputDir.x, inputDir.y) * Mathf.Rad2Deg + cam.eulerAngles.y;
            transform.eulerAngles = Vector3.up * Mathf.SmoothDampAngle(transform.eulerAngles.y, targetRotation, ref turnSmoothVelocity, turnSmoothTime);

        }

        if (isJumping)
        {
            y_vel = Mathf.Sqrt(-2 * gravity * jumpHeight);
        }

        y_vel += Time.deltaTime * gravity;

        bool running = Input.GetKey(KeyCode.LeftShift);

        float targetspeed = ((running) ? runSpeed : walkSpeed) * inputDir.magnitude;

        currentSpeed = Mathf.SmoothDamp(currentSpeed, targetspeed, ref speedSmoothVelocity, speedSmoothTime);
        
        controller.Move(transform.forward * currentSpeed * Time.deltaTime + Vector3.up * y_vel * Time.deltaTime);

        if (controller.isGrounded)
        {
            y_vel = 0;
        }

        refSpeed = new Vector2(controller.velocity.x, controller.velocity.z).magnitude;

        float animatorSpeedPercent = ((running) ? refSpeed/runSpeed : refSpeed/walkSpeed * 0.5f) * inputDir.magnitude;
        animator.SetFloat("speedPercent", animatorSpeedPercent);

    }
}
