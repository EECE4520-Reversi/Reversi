import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser, registerUser } from "../services/backendservice";
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
    <div className="grid justify-center place-items-center h-[85%]">
      <div className="grid grid-cols-1 gap-5">
      <div className="grid grid-cols-2">
        <label className="col-span-1 mx-2 text-4xl">Username</label>
        <input
          className="col-span-1 text-white w-full px-2 bg-transparent rounded border border-blue-500"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        ></input>
      </div>

      <div className="grid grid-cols-2">
        <label className="text-4xl">Password</label>
        <input
          className="col-span-1 text-white w-full px-2 bg-transparent rounded border border-blue-500"
          placeholder="Password"
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

      <div className="grid grid-cols-1 place-items-center gap-3">
        <button
          className="w-1/2 btn-primary"
          onClick={handleLogin}
        >
          {hasAccount ? "Login" : "Register"}
        </button>
        <button
          className="w-1/2 btn-primary"
          onClick={() => navigate("/")}
        >
          Cancel
        </button>
      </div>

      <h1 className="text-white">{errorMsg}</h1>
      </div>
    </div>
  );
};

export default Login;
