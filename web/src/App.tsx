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
import { GameData } from "./types/GameData";

const App = () => {
  const [userData, setUserData] = useState<UserData | undefined>();
  const [gameData, setGameData] = useState<GameData>();
  const [boardID, setBoardID] = useState<string>("");

  useEffect(() => {
    socket.on("players", (data: string[]) => {
      console.log(`Online players: ${data}`);
    });

    socket.on("board", (data: GameData) => {
      if (data.id != boardID) return;
      setGameData(data);
      console.log(data);
    });
  }, [boardID]);

  return (
    <>
      <CustomParticles />
      <Nav userData={userData} setUserData={setUserData} />
      <Routes>
        <Route
          path="/"
          element={<Home gameData={gameData} setBoardID={setBoardID} />}
        />
        <Route
          path="/game"
          element={<Game gameData={gameData} boardID={boardID} />}
        />
        <Route path="/login" element={<Login setUserData={setUserData} />} />
      </Routes>
    </>
  );
};

export default App;
