import { data } from 'autoprefixer'
import React, {useEffect,useState} from 'react'

export default function index() {

  
  const [message,setMessage] = useState('loading')

  useEffect(()=>{
    fetch('http://localhost:8080/api/home').then(
     res=> res.json()
    ).then(
      data=>{
        console.log(data.message)
        setMessage(data.message)
      }
    )
  },[data])

  return (
    <div>
      {message}
    </div>
  )
}
