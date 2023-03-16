import { ReactElement } from "react";

export default function Modal({
  onClose,
  onSubmit,
  title,
  component,
  submitText,
}: {
  onSubmit: () => void;
  onClose: () => void;
  title: string;
  submitText: string;
  component: ReactElement;
}) {
  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-auto my-6 mx-auto max-w-3xl">
          <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-stone-800 outline-none focus:outline-none">
            <div className="flex items-start justify-between p-5 border-b border-solid border-slate-200">
              <h3 className="text-3xl font-semibold">{title}</h3>
            </div>
            <div className="relative p-6 flex-auto">
              <>{component}</>
            </div>
            <div className="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
              <button
                className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button"
                onClick={onClose}
              >
                Close
              </button>
              <button
                className="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button"
                onClick={onSubmit}
              >
                {submitText}
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
    </>
  );
}
