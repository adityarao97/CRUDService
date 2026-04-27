import { useEffect, useState } from 'react';
import TextForm from './components/TextForm';
import TextList from './components/TextList';
import { createText, getAllTexts } from './api';

function App() {
    const [texts, setTexts] = useState([]);
    const [error, setError] = useState('');

    const loadTexts = async () => {
        try {
            const result = await getAllTexts();
            setTexts(result);
            setError('');
        } catch (err) {
            setError('Failed to fetch texts');
        }
    };

    useEffect(() => {
        loadTexts();
    }, []);

    const handleSubmit = async (content) => {
        try {
            await createText(content);
            await loadTexts();
        } catch (err) {
            setError('Failed to save text');
        }
    };

    return (
        <div>
            <h1>Text CRUD App</h1>
            <TextForm onSubmit={handleSubmit} />
            {error && <p>{error}</p>}
            <TextList texts={texts} />
        </div>
    );
}

export default App;