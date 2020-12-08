import { React } from 'react';
import { Form } from 'react-bootstrap'


const FormMedicalDayUnit = () => {
    return (
        <div>

            <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Does the PI have a medical appointment with BCCH </Form.Label>
                <Form.Control as="select">
                    <option>Yes</option>
                    <option>No</option>
                </Form.Control>
            </Form.Group>


            <Form.Group controlId="exampleForm.ControlTextarea1">
                <Form.Label>Additional comments for MDU</Form.Label>
                <Form.Control as="textarea" rows={3} />
            </Form.Group>

        </div>
    )
}

export default FormMedicalDayUnit