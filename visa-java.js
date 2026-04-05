const express = require('express');
const axios = require('axios');
const app = express();

app.get('/visa-requirements', async (req, res) => {
  const { origin, destination, purpose } = req.query;

  try {
    const response = await axios.get(`https://api.travelbuddy.ai/visa-requirements`, {
      params: { origin, destination, purpose }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Error fetching visa information');
  }
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
