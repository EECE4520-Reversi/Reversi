import { Dispatch, SetStateAction, useState } from "react";
import { createGame } from "../services/backendservice";
import Modal from "./Modal";


const NewGame = ({setGameData}: {
    setGameData: Dispatch<SetStateAction<object>>
}) => {

    const [visible, setVisible] = useState<boolean>(false);
    const [boardSize, setBoardSize] = useState<number>(8);
    const [difficulty, setDifficulty] = useState<"Easy" | "Medium" | "Hard">("Medium");

    const onSubmit = () => {
        createGame(boardSize, difficulty).then(gameData => {
            setGameData(gameData);
            setVisible(false);
        })
    }

    const newGameComponents = 
        <div>
            <div className="m-1">
                <h2 className="inline p-2 text-xl">Board Size:</h2>
                <input
                    type="number"
                    className="rounded w-10 text-black px-2"
                    onChange={(event) => setBoardSize(parseInt(event?.target.value))}
                    value={boardSize}
                    />
            </div>
            <div className="mt-3">
                <h2 className="inline p-2 text-xl">Difficulty:</h2>
                <div className="flex justify-between">
                    <div className="flex items-center" onClick={() => setDifficulty("Easy")}>
                        <input id="difficulty-radio-1" type="radio" name="difficult-radio" className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600" />
                        <label htmlFor="difficulty-radio-1" className="font-medium">Easy</label>
                    </div>
                    <div className="flex items-center" onClick={() => setDifficulty("Medium")}>
                        <input defaultChecked id="difficulty-radio-2" type="radio" name="difficult-radio" className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600" />
                        <label htmlFor="difficulty-radio-2" className="font-medium">Medium</label>
                    </div>
                    <div className="flex items-center" onClick={() => setDifficulty("Hard")}>
                        <input id="difficulty-radio-3" type="radio" name="difficult-radio" className="w-4 h-4 focus:ring-gray-600 ring-offset-gray-800 focus:ring-2 bg-gray-700 border-gray-600" />
                        <label htmlFor="difficulty-radio-3" className="font-medium">Hard</label>
                    </div>
                </div>
            </div>
        </div>
        

    return (
        <div>
            <button
            className="bg-pink-500 text-white active:bg-pink-600 px-6 py-3 rounded"
            type="button"
            onClick={() => setVisible(true)}
            >
                New Game
            </button>
            
            {visible && <Modal onSubmit={onSubmit} onClose={() => setVisible(false)} title="New Game" submitText="Create" component={newGameComponents}/>}
        </div>
    );

}

export default NewGame;