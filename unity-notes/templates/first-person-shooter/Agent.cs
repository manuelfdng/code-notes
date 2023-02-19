using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Agent : MonoBehaviour
{
    public GameObject player;
    NavMeshAgent zombie;
    public Animator animator;


    void Start()
    {
        zombie = GetComponent<NavMeshAgent>();
        
    }

    void Update()
    {
        zombie.destination = player.transform.position;
        animator.SetFloat("velForward", zombie.velocity.magnitude / zombie.speed);
    }
}
