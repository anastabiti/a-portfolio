import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Searchbar } from "./components/Searchbar.1";
import { Profilebar } from "./components/Profilebar";
import { Cards } from "./components/Cards";
function App() {
  const innerWidth = window.innerWidth;
  const innerHeight = window.innerHeight;
  return (
    <>
      <div className="mylogo">
        <img src="/mylogo.png" className="mylogo"></img>
      </div>

      <Searchbar></Searchbar>

      <Profilebar></Profilebar>
      <Cards></Cards>
      <div className="welcome">
        Welcome to Shop<span>Easy</span>
      </div>
    </>
  );
}
export default App;
