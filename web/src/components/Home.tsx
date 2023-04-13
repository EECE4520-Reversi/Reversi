const Home = () => {
  return <div className="flex justify-center items-center h-[85%]">

    <div className="grid grid-cols-3 w-1/2 gap-10">
      <h1 className="col-span-3 text-9xl font-bold">Reversi</h1>


      <div className="col-span-3 gap-5 flex">
        <button className="text-4xl w-1/2 btn-primary">Create Game</button>
        <button className="text-4xl w-1/2 btn-primary">Join Game</button>
      </div>
    </div>


  </div>;
};

export default Home;
