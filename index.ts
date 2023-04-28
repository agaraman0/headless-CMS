import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [pages, setPages] = useState([]);
  const [images, setImages] = useState([]);

  useEffect(() => {
    axios.get('/pages')
      .then(response => {
        setPages(response.data);
      });

    axios.get('/images')
      .then(response => {
        setImages(response.data);
      });
  }, []);

  return (
    <div>
      {pages.map(page => (
        <div key={page.id}>
          <h1>{page.title}</h1>
          <div dangerouslySetInnerHTML={{ __html: 
page.content }} />
        </div>
      ))}

      {images.map(image => (
        <div key={image.id}>
          <h2>{image.name}</h2>
          <img 
src={`https://cdn.example.com/${image.filename}`} 
alt={image.name} />
        </div>
      ))}
    </div>
  );
};

export default App;

