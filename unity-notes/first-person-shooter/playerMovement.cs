using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playerMovement : MonoBehaviour
{
    #region Variables
    Vector3 velocity;
    Vector3 moveDirection;

    [SerializeField]
    float walkSpeed = 3f;

    [SerializeField]
    float runSpeed = 5f;

    float speed;

    [SerializeField]
    float jumpHeight = 0.5f;

    CharacterController controller;

    public Transform groundChecker;

    [SerializeField]
    float gravity = -9.8f;

    bool isRunning;
    bool isJumping;
    bool isGrounded;
    bool jumpToggle;

    public LayerMask groundMask;

    #endregion
    void Start()
    {
        controller = GetComponent<CharacterController>();
    }

    void Update()
    {
        GroundChecker();
        GetKeyboardInputs();
        CheckJumpingStates();
        PlayerMovement();

    }

    void GetKeyboardInputs()
    {
        velocity.x = Input.GetAxis("Horizontal");
        velocity.z = Input.GetAxis("Vertical");

        isRunning = Input.GetKey(KeyCode.LeftShift);
        isJumping = Input.GetKeyDown(KeyCode.Space);
    }

    void GroundChecker()
    {
        isGrounded = Physics.CheckSphere(groundChecker.position, 0.3f, groundMask);
        
    }

    void CheckJumpingStates()
    {
        if (isJumping && isGrounded) //initiates jump
        {
            velocity.y = Mathf.Sqrt(-3 * gravity * jumpHeight);
            jumpToggle = true;
        }

        else if (!isGrounded && jumpToggle) //jumps and falls back slowly
        {
            velocity.y += gravity * Time.deltaTime;
        }

        else if (isGrounded) //isGrounded
        {
            velocity.y = gravity;
            jumpToggle = false;
        }

        else if (!isGrounded && !jumpToggle) //falls of cliff but not jumping
        {
            velocity.y += gravity * Time.deltaTime;
        }
    }

    void PlayerMovement()
    {
        speed = (isRunning) ? runSpeed : walkSpeed;
        moveDirection = (transform.forward * velocity.z + transform.right * velocity.x).normalized +
                         transform.up * velocity.y;

        controller.Move(moveDirection * Time.deltaTime * speed);
    }
}
