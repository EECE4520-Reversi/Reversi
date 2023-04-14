import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import Game from "./components/Game";
import Login from "./components/Login";
import { UserData } from "./types/UserData";
import "./App.css";
import socket from "./services/websocket";
import Home from "./components/Home";
import Nav from "./components/Nav";
import CustomParticles from "./components/Particles";

const App = () => {
  const [userData, setUserData] = useState<UserData | undefined>();

  useEffect(() => {
    socket.on("players", (data: string[]) => {
      console.log(`Online players: ${data}`)
    })
  }, [])

  return (
    <>
      <CustomParticles />
      <Nav userData={userData} setUserData={setUserData} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/game"
          element={<Game userData={userData} setUserData={setUserData} />}
        />
        <Route path="/login" element={<Login setUserData={setUserData} />} />
      </Routes>
    </>
  );
};

export default App;
