import { useNavigate } from "react-router-dom";
import { UserData } from "../types/UserData";
import socket from "../services/websocket";

const Nav = ({
  userData,
  setUserData,
}: {
  userData: UserData | undefined;
  setUserData: (data: UserData | undefined) => void;
}) => {
  const navigate = useNavigate();

  const loginOrOut = () => {
    if (!userData) {
      navigate("/login");
      return;
    }
    socket.emit('logout')
    setUserData(undefined);
  };

  return (
    <div className="flex justify-end">
      <div>
        <button
          className="bg-transparent mr-5 hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
          onClick={loginOrOut}
        >
          {userData ? "Logout" : "Login"}
        </button>
      </div>

      {userData && (
        <h1 className="text-3xl">
          {userData?.username} ({userData?.elo} ELO)
        </h1>
      )}
    </div>
  );
};

export default Nav;
