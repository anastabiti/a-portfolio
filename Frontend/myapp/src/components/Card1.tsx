export function Card1()
{
    return (
        <div className="card1">
        <h1 style={{fontFamily:"Poppins",color:"white",position:"absolute"}}>$1999</h1>
        <img src="laptop.png" width={250} height={220} style={{float:"right", overflowX:"auto"}}></img>   
        <button style={{position:'absolute',top:"80%", background:"white", borderRadius:"20px",
width:"120px",height:"55px"}}> <h4 style={{color:"red",fontFamily:"Poppins"}}>Add to cart</h4> </button>
        </div>
    );
}