import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser, registerUser } from "../services/backendservicews";
import { UserData } from "../types/UserData";

const Login = ({ setUserData }: { setUserData: (data: UserData) => void }) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errorMsg, setErrorMsg] = useState<string>("");
  const [hasAccount, setHasAccount] = useState<boolean>(true);
  const navigate = useNavigate();

  const handleLogin = () => {
    const func = hasAccount ? loginUser : registerUser;

    func(username, password)
      .then((data) => {
        console.log(data);
        setUserData(data);
        navigate("/");
      })
      .catch((err) => {
        console.log(err);
        setErrorMsg(err.response.data.detail);
      });
  };

  return (
    <div className="grid justify-center place-items-center m-36 p-28 rounded-xl shadow-2xl">
      <div className="grid grid-cols-2">
        <label className="col-span-1 mx-2 my-2 text-4xl">Username</label>
        <input
          className="col-span-1 text-black  px-2 my-2  rounded"
          placeholder="username"
          onChange={(e) => setUsername(e.target.value)}
        ></input>
      </div>

      <div className="grid grid-cols-2">
        <label className="mx-2 my-2 text-4xl">Password</label>
        <input
          className="col-span-1 text-black px-2 my-2 rounded"
          placeholder="password"
          onChange={(e) => setPassword(e.target.value)}
          type="password"
        ></input>
      </div>
      <h1
        className="text-lg cursor-pointer"
        onClick={() => setHasAccount(!hasAccount)}
      >
        {hasAccount ? "Need to register?" : "Need to log in?"}
      </h1>

      <div>
        <button
          className="m-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
          onClick={handleLogin}
        >
          {hasAccount ? "Login" : "Register"}
        </button>
      </div>

      <div>
        <button
          className="m-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
          onClick={() => navigate("/")}
        >
          Cancel
        </button>
      </div>

      <h1 className="text-white">{errorMsg}</h1>
    </div>
  );
};

export default Login;
