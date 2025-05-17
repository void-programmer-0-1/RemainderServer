import React, { useEffect, useState } from "react";


const fetchData = async(setData, setLoading, setError) => {
  try {
    setLoading(true);
    const response = await fetch("http://127.0.0.1:8000/");
    if(!response.ok){
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    setData(data);
  }
  catch (error){
    setError(error.message);
  }
  finally {
    setLoading(false);
  }
}



function App() {

  const [data, setData] = useState({});
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  
  useEffect(() => {
    fetchData(setData, setLoading, setError);
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error != "") return <p>Error: {error}</p>

  return (
    <div className="flex items-center justify-center bg-gray-100 min-h-screen bg-gray-100">
      <div className="p-5 bg-white rounded-2xl shadow-md hover:shadow-lg transition-shadow duration-300 hover:bg-gray-50 cursor-pointer">
        <h1 className="text-2xl font-bold mb-2 text-gray-800">Message:</h1>
        <ul className="list-disc pl-5">
          <li className="text-lg text-gray-600 hover:text-gray-800 transition-colors">
            {data.message}
          </li>
        </ul>
      </div>
    </div>
  );
}

export default App
