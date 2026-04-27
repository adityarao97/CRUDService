import { useState } from 'react';

function TextForm({ onSubmit }) {
    const [content, setContent] = useState('');

    const handleFormSubmit = (event) => {
        event.preventDefault();

        if (!content.trim()) {
            return;
        }

        onSubmit(content);
        setContent('');
    };

    const handleChange = (event) => {
        setContent(event.target.value);
    };

    return (
        <div>
            <form onSubmit={handleFormSubmit}>
                <label>Enter Text</label>
                <input value={content} onChange={handleChange} />
                <button type="submit">Save</button>
            </form>
        </div>
    );
}

export default TextForm;