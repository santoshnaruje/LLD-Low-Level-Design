package Observer;

/**
 * Observer Interface
 * 
 * This interface defines the contract for objects that want to be notified
 * of changes in the Observable (Subject).
 * 
 * Key Method:
 * - update(): Called by the Observable when its state changes
 */
public interface Observer {
    void update();
}
