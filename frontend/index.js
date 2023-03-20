const APIURL = "http://localhost:3000/stats"
const dateFormat = (timestamp) =>{
    return new Date(timestamp*1000).toLocaleString("de-DE")
}
const loadRecent = async () => {
    const table = document.querySelector("#recent")
    const res = await (await fetch(APIURL + "/recent")).json()
    res.forEach(e => {
        table.innerHTML += `
        <tr>
        <td>${e.tweets_scraped}</td>
        <td>${dateFormat(e.time_started)}</td>
        <td>${dateFormat(e.time_finished)}</td>
        <td>${e.time_finished - e.time_started} seconds</td>
        </tr>
        `
    });
}
const loadLogs = async () => {
    const table = document.querySelector("#log")
    const res = await (await fetch(APIURL + "/log")).json()
    res.forEach(e => {
        table.innerHTML += `
        <tr>
        <td>${e.instance}</td>
        <td>${e.msg}</td>
        <td>${dateFormat(e.time_logged)}</td>
        </tr>
        `
    });
}
const loadTotal = async () => {
    const h1 = document.querySelector("#total")
    const res = await (await fetch(APIURL + "/amount")).json()
    h1.innerHTML = `Scraped ${res[0].amount} tweets in total`
}
loadRecent()
loadLogs()
loadTotal()