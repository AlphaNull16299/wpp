const { spawn } = require('child_process');
const { createServer } = require('http');
const app = createServer();
app.on('request',(req,res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain; char="utf8"' });
  res.write('untiiiiiiiiiiiiiijiiii');
  res.end();
});
app.listen(3000);
spawn('sh',['main.sh'],{ stdio: [process.stdin,process.stdout,process.sterr] });