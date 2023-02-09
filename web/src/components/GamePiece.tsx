import { useState } from "react";


export const GamePiece = ({isFlipped}: {
    isFlipped: boolean
}) => {

    const [flipped, setFlipped] = useState(isFlipped);

    const onClick = () => {
        setFlipped(!flipped);
    }

    return (
        <div className={`${flipped ? "rotate-x-180" : "rotate-x-0"} hover:cursor-pointer`} onClick={onClick}>
            <div className={`${flipped ? " bg-black" : "bg-white"} delay-300 rounded-full w-12 h-12`} />
        </div>
    );
}