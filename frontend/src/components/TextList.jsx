function TextList({ texts }) {
    const renderedTexts = texts.map((text) => {
        return <li key={text.id}>{text.content}</li>;
    });

    return (
        <div>
            <h2>Saved Texts</h2>
            <ul>{renderedTexts}</ul>
        </div>
    );
}

export default TextList;