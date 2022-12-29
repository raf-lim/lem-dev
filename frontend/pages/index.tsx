import { useState } from "react";

const Home = () => {
  const [state, setState] = useState(1);
  return (
    <>
      <p>{state}</p>
      <button onClick={() => setState(state + 1)}>Click me!</button>
    </>
  );
};

export default Home;
