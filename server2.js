const tls = require('tls');

const serverName = 'localhost';
const serverPort = 3000;

const options = {
  host: serverName,
  port: serverPort,
};

const socket = tls.connect(options, () => {
  console.log('Connected');

  const negotiatedProtocol = socket.getProtocol();
  console.log(`Negotiated Protocol: ${negotiatedProtocol}`);

  const tlsVersion = socket.getProtocol().replace('TLSv', '');
  console.log(`TLS Version: ${tlsVersion}`);

  socket.end();
});

socket.on('error', (error) => {
  console.error('Error:', error);
});