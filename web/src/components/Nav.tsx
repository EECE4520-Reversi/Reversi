import { useNavigate } from "react-router-dom";
import { UserData } from "../types/UserData";

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

    setUserData(undefined);
  };

  return (
    <div className="flex justify-between">

      <div className="flex gap-3">
        <button className="btn-primary" onClick={() => navigate("/")}>Home</button>
        <button className="btn-primary" onClick={() => navigate("/leaderboard")}>Leaderboard</button>
      </div>

      <div className="justify-end">
      <div>
        <button className="btn-primary" onClick={loginOrOut}>
          {userData ? "Logout" : "Login"}
        </button>
      </div>

      {userData && (
        <h1 className="text-3xl">
          {userData?.username} ({userData?.elo} ELO)
        </h1>
      )}
      </div>
    </div>
  );
};

export default Nav;
