import { useEffect, useState } from "react";
import { makeMove } from "../services/backendservice";


export const GamePiece = ({state, idx}: {
    state: number,
    idx: number
}) => {
    
    const colors = ["bg-black", "bg-white"];
    const [colorIndex, setColorIndex] = useState(state);
    const [color, setColor] = useState(colors[colorIndex]);
    const [angle, setAngle] = useState<number>(0);

    const onClick = () => {
        setColorIndex((colorIndex + 1) % colors.length);
        setAngle(angle == 0 ? 180 : 0);
        makeMove(idx)
    }

    useEffect(() => {
        setColor(colorIndex < colors.length ? colors[colorIndex] : "bg-transparent")
    }, [colorIndex])

    return (
        <div className={`rotate-x-${angle} hover:cursor-pointer`} onClick={onClick}>
            <div className={`${color} delay-300 rounded-full w-12 h-12`} />
        </div>
    );
}