const mysql = require("mysql2");
const dotenv = require("dotenv").config().parsed
const connection = mysql.createPool({
    host: dotenv.host,
    user: dotenv.user,
    password: dotenv.password,
    database: dotenv.database,
    connectionLimit: 5
});
exports.query = (QUERY, DATA) => {
  return new Promise((resolve) => {
    connection.execute(QUERY, DATA, (err, results) => {
      resolve({ err: Boolean(err), rows: results });
    });
    
  });
};