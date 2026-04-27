import axios from "axios";

const BASE_URL = "http://localhost:5000";

export const createText = async (content) => {
  const response = await axios.post(`${BASE_URL}/texts`, {
    content: content,
  });
  return response.data;
};

export const getAllTexts = async () => {
  const response = await axios.get(`${BASE_URL}/texts`);
  return response.data;
};
