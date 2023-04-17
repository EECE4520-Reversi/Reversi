import { ReactElement } from "react";

export default function Modal({
  visible,
  setVisibility,
  onSubmit,
  title,
  component,
  submitText,
}: {
  onSubmit?: () => void;
  setVisibility: (visiblitity: boolean) => void;
  title: string;
  submitText: string;
  component?: ReactElement;
  visible: boolean;
}) {
  if (!visible) return <></>;

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
            <div className="flex items-center justify-between p-6 border-t border-solid border-slate-200 rounded-b">
              <button
                className="btn-secondary"
                type="button"
                onClick={() => setVisibility(false)}
              >
                Close
              </button>

              {onSubmit && (
                <button
                  className="btn-primary"
                  type="button"
                  onClick={() => {
                    setVisibility(false);
                    onSubmit();
                  }}
                >
                  {submitText}
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
    </>
  );
}
