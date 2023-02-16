import { useEffect, useState } from 'react';
import './App.css'
import { GamePiece } from './components/GamePiece'
import { fetchBoard } from './services/backendservice';

function App() {

  const [width, setWidth] = useState<number>(12);
  const [height, setHeight] = useState<number>(12);

  const [board, setBoard] = useState<number[]>([]);

  useEffect(() => {
    fetchBoard().then(data => {
      setBoard(data);
    })
  }, [])


  return (
    <div className="container">
      <p className="text-8xl text-white-200 font-bold mb-5">
        Reversi
        </p>

        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" 
          onClick={() => setWidth(width - 1)}>Decrease Width</button>
        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" 
          onClick={() => setHeight(height - 1)}>Decrease Height</button>

        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" 
          onClick={() => setWidth(width + 1)}>Increase Width</button>
        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" 
          onClick={() => setHeight(height + 1)}>Increase Height</button>

        <div className="min-h-screen flex items-center justify-center">
        <div className={`grid grid-cols-${width} grid-rows-${height} gap-1`}>
          {
            board.map((e, i) => <GamePiece key={i} state={e}/>)
          }
        </div>
      </div>
    </div>
  )
}

export default App
