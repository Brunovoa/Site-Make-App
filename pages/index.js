function Home() {
    return <div>
        <h1>Home</h1>
        <contador />
        <div>teste</div>
    </div>
}

function contador() {
    const [contador,setContador] = usestate(1)

    function adicionarContador() {
        setContador(contador + 1)
    }
    return (
        <div>
            <div>
                contador
            </div>
            <button onClick={adicionarContador}>
                adicionar
            </button>
        </div>
    )
}

export default Home