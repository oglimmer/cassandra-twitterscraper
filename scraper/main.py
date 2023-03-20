import scraper, tasks, time, conn

tasks.log("starting up...")
session = conn.getSession()
tasks.log("connected to cluster...")
prepStatement = conn.getPreparedStatement(session=session)
tasks.log("prepared statement ready...")

while True:
    tasks.log("sleeping before requesting new task...")
    time.sleep(5)
    task = tasks.getTask()
    if task == None:
        tasks.log("not retrieving any more tasks, exiting...")
        exit(0)
    amount = scraper.scrape(task=task, session=session, prepStatement=prepStatement)
    tasks.log(f"{amount} tweets scraped")
    tasks.commitTask(task, amount)