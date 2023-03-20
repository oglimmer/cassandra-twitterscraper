const app = require("express")()
app.use(require("cors")({
    origin: "*"
}))
const {query} = require("./database")
app.get("/stats/log", async (req, res) => {
    try{
    const dbres = await query("SELECT * FROM log ORDER BY id DESC LIMIT 20")
    if(dbres.err) throw new Error()
    res.send(dbres.rows)
    }catch(e){
        res.status(500).send()
    }
})
app.get("/stats/amount", async (req, res)=>{
    try{
        const dbres = await query("SELECT stat_value AS amount FROM stats WHERE stat_name = ?",
        ["tweets_scraped"])
        if(dbres.err) throw new Error()
        res.send(dbres.rows)
    }catch(e){
            res.status(500).send()
    }
})
app.get("/stats/recent", async (req, res)=>{
    try{
        const dbres = await query("SELECT * FROM tasks WHERE done = ? ORDER BY time_finished LIMIT 20",
        [1])
        if(dbres.err) throw new Error()
        res.send(dbres.rows)
    }catch(e){
            res.status(500).send()
    }
})
app.listen(3000)