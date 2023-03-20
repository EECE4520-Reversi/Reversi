import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser, registerUser } from "../services/backendservice";
import { UserData } from "../types/UserData";



const Login = ({setUserData}: {
    setUserData: (data: UserData)=>void
}) =>{
    const [username, setUsername] = useState <string>("");
    const [password, setPassword] = useState <string>("");
    const [errorMsg, setErrorMsg] = useState <string>("");
    const navigate = useNavigate()

    const handleLogin = () =>{
        loginUser(username, password).then((data)=>{
            console.log(data)
            setUserData(data)
            navigate("/")
        }).catch((err)=>{
            console.log(err)
            setErrorMsg(err.response.data.detail)
        })
    } 

    const handleRegister = () =>{
        registerUser(username, password).then((data)=>{
            console.log(data)
            setUserData(data)
            navigate("/")
        }).catch((err)=>{
            console.log(err)
            setErrorMsg(err.response.data.detail)
        })
    } 

    return <div>
        <label className="mx-2 my-2">username</label>
        <input className="text-black px-2 my-2" onChange={(e)=>setUsername(e.target.value)}></input>
        <br></br>
        <label className="mx-2 my-2">password</label>
        <input className="text-black px-2 my-2"  onChange={(e)=>setPassword(e.target.value)} type="password"></input>
        <br></br>
        <button className="m-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={handleLogin}>Login</button>
        <br></br>
        <button className="m-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={handleRegister}>Register</button>
        <br></br>
        <button className="m-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={()=>navigate("/")}>Cancel</button>
        <br></br>
        <h1 className="text-white">{errorMsg}</h1>
        </div>
}

export default Login