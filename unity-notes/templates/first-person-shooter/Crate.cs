using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Crate : MonoBehaviour
{
    public GameObject fracturedCrate;

    public void Explode()
    {
        Destroy(gameObject);
        GameObject cratePieces = Instantiate(fracturedCrate, gameObject.transform.position, Quaternion.identity);
        Destroy(cratePieces, 10f);
        
    }
}
