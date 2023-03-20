import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Game from "./components/Game";
import Login from "./components/Login";
import { UserData } from "./types/UserData";
import "./App.css";

const App = () => {
  const [userData, setUserData] = useState<UserData | undefined>();

  return (
    <>
      <Routes>
        <Route
          path="/"
          element={<Game userData={userData} setUserData={setUserData} />}
        />
        <Route path="/login" element={<Login setUserData={setUserData} />} />
      </Routes>
    </>
  );
};

export default App;
