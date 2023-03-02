import { useState } from "react";
import Modal from "./Modal";


const NewGameModal = () => {

    const [visible, setVisible] = useState<boolean>(false);
    const [boardWidth, setBoardWidth] = useState<number>(8);
    const [boardHeight, setBoardHeight] = useState<number>(8);


    const boardSizeSelector = 
        <div>
            <div className="m-1">
                <h2 className="inline p-2">Board Height</h2>
                <input
                    type="number"
                    className="rounded w-10 text-black px-2"
                    onChange={(event) => setBoardHeight(parseInt(event?.target.value))}
                    value={boardHeight}
                    />
            </div>
            <div>
                <h2 className="inline p-2">Board Width </h2>
                <input
                    type="number"
                    className="rounded w-10 text-black px-2"
                    onChange={(event) => setBoardWidth(parseInt(event?.target.value))}
                    value={boardWidth}
                    />
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

            <Modal visible={visible} onClose={() => setVisible(false)} title="New Game" submitText="Create" components={[boardSizeSelector]}/>
        </div>
    );

}

export default NewGameModal;