const express = require("express")

const app = express()

app.get("/",(req,res)=>{
    console.log("Content-Type : ", req.header["Content-Type"]);  
    res.json({
        message: "header test successfully"
    })
})

app.listen(3000, ()=> {
    console.log("Server is running on http://localhost:3000");
})

