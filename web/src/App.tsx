import './App.css'
import Board from './components/Board'
import Modal from './components/Modal'
import NewGameModal from './components/NewGame'

function App() {

  return (
    <div className="container">
        <h1 className="text-8xl text-white-200 font-bold mb-5">
          Reversi
        </h1>

        <NewGameModal />
        <Board />

    </div>
  )
}

export default App
