import { useNavigate } from "react-router-dom"

const Nav = ()=>{
    const navigate = useNavigate()

    return <div className="w-full h-10">
        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={()=>{
            navigate("/login")
        }}>Login</button>
    </div>
}

export default Nav