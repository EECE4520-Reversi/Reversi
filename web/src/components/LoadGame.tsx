import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Modal from "./Modal";
import socket from "../services/websocket";
import { LoadableGame } from "../types/LoadableGame";
import { useNavigate } from "react-router";

const LoadGame = ({
    setBoardID,
}: {
    setBoardID: Dispatch<SetStateAction<string>>;
}) => {
    const [openGames, setOpenGames] = useState<LoadableGame[]>([]);
    const [loadModalOpen, setLoadModalOpen] = useState<boolean>(false);
    const [selectedGameID, setSelectedGameID] = useState<string>();
    const navigate = useNavigate();

    useEffect(() => {
        socket.emit("loadableGames", (data: LoadableGame[]) => setOpenGames(data));
        socket.on("openGames", (data: LoadableGame[]) => setOpenGames(data));
    }, []);

    const loadGame = () => {
        if (selectedGameID) {
            setBoardID(selectedGameID);
            socket.emit("loadGame", selectedGameID);
            console.log(`Loading Game: ${selectedGameID}`);
            navigate("/game");
        }
    };

    const openGamesComponents = (
        <div className="min-w-[25vw]">
            {openGames.map((game) => (
                <div
                    className={`btn-primary cursor-pointer text-2xl px-3 py-1 ${selectedGameID == game.id ? "bg-blue-500 text-white" : ""
                        }`}
                    onClick={() => setSelectedGameID(game.id)}
                >
                    <h1>
                        {gameDisplayText(game)}
                    </h1>
                </div>
            ))}
        </div>
    );

    return (
        <>
            <button
                onClick={() => setLoadModalOpen(true)}
                className="text-4xl w-1/2 btn-primary"
            >
                Load Game
            </button>
            <Modal
                onSubmit={loadGame}
                visible={loadModalOpen}
                setVisibility={setLoadModalOpen}
                title="Your Games"
                submitText="Load"
                component={openGamesComponents}
            />
        </>
    );
};

const GameTypeMap = {
    1: "Local",
    2: "AI",
    3: "Online",
}

const DifficultyMap = {
    0: "Easy",
    1: "Medium",
    2: "Hard",
}

const StatusMap = {
    0: "Over",
    1: "Ongoing",
}

function gameDisplayText(game: LoadableGame) {
    switch (game.type) {
        case 1:
            return `${GameTypeMap[game.type]}: ${game.size}x${game.size} | ${game.status ? "Ongoing" : "Over"}`
        case 2:
            return `${GameTypeMap[game.type]}: ${DifficultyMap[game.difficulty]} | ${game.size}x${game.size} | ${game.status ? "Ongoing" : "Over"}`
        case 3:
            return `${GameTypeMap[game.type]}: ${game.players[0]} vs ${game.players[1]} | ${game.size}x${game.size} | ${game.status ? "Ongoing" : "Over"}`

    };
};

export default LoadGame;
