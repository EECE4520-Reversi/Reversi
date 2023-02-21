import { useEffect, useState } from 'react';
import './App.css'
import { GamePiece } from './components/GamePiece'
import { fetchBoard, resetBoard } from './services/backendservice';

function App() {

  const [width, setWidth] = useState<number>(8);
  const [height, setHeight] = useState<number>(8);

  const [board, setBoard] = useState<number[]>([]);
  const [score, setScore] = useState<number>(0);
  const [gameState, setGameState] = useState<number>(0);

  const updateInternalState = (data: any) => {
    console.log(data);
    setBoard(data.board);
    setScore(data.score);
    setGameState(data.state);
  }

  const updateBoard = () => {
    fetchBoard().then(updateInternalState)
  }

  const emptyBoard = () => {
    resetBoard().then(updateInternalState)
  }

  useEffect(() => {
    updateBoard()
  }, [])


  return (
    <div className="container">
        <h1 className="text-8xl text-white-200 font-bold mb-5">
          Reversi
        </h1>

        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" 
          onClick={emptyBoard}>Reset</button>

        <h3>Score: {score}</h3>
        <h3>State: {gameState}</h3>

        <div className="flex items-center justify-center">
        <div className={`grid grid-cols-${width} grid-rows-${height}`}>
          {
            board.map((e, i) => <GamePiece key={i} idx={i} state={e} gameState={gameState} updateBoard={updateBoard}/>)
          }
        </div>
      </div>
    </div>
  )
}

export default App
