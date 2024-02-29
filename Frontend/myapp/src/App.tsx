import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Searchbar } from "./components/searchBar";
function App() {
  return (
    <>
    <Searchbar>
      sdsd
    </Searchbar>
      {/* <form>
        <input type="text" placeholder="Search..." />
        <button type="submit">Search</button>
      </form> */}

      <div className="mylogo">
        <img src="/mylogo.png" width={200}></img>
      </div>
      <div className="welcome">
        Welcome to Shop<span>Easy</span>{" "}
      </div>
    </>
  );
}
export default App; 